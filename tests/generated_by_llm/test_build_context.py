import pytest
from unittest.mock import patch, MagicMock
from build_context import analyze_repository, get_git_info

class TestBuildContext:
    def test_get_git_info(self):
        # Mock subprocess.check_output to return different branch and commit
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.side_effect = [
                "feature-branch\n",  # First git command should work
                "0123456789abcdef"   # Second git command should fail
            ]
            result = get_git_info()
            assert result == {"branch": "feature-branch", "commit": "0123456789abcdef"}

    def test_analyze_repository(self):
        # Mock subprocess.check_output for different outcomes
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.side_effect = [
                "main.py\nutils.py"   # List of Python files
            ]
            
            context = analyze_repository()
            
            assert context["repository_info"]["branch"] == "feature-branch"
            assert context["repository_info"]["commit"] == "0123456789abcdef"
            assert len(context["files"]) == 4
            assert "main.py" in [f["path"] for f in context["files"]]
            assert "utils.py" in [f["path"] for f in context["files"]]
            assert context["metadata"]["total_files"] == 4
            assert context["metadata"]["changed_files"] == 2
        
        # Mock subprocess.check_output to fail
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.side_effect = Exception("Git command failed")
            with pytest.raises(Exception):
                analyze_repository()
        
        # Edge case: No changed files
        mock_check_output.side_effect = ["no-changed-files"]
        context = analyze_repository()
        assert len(context["files"]) == 0
        assert context["metadata"]["total_files"] == 0
        assert context["metadata"]["changed_files"] == 0

    def test_get_git_info_edge_case(self):
        # Mock subprocess.check_output to return a different branch and commit
        with patch('subprocess.check_output') as mock_check_output:
            mock_check_output.side_effect = [
                "stable-branch\n",  # First git command should work
                "9876543210abcdef"   # Second git command should fail
            ]
            result = get_git_info()
            assert result == {"branch": "stable-branch", "commit": "9876543210abcdef"}

if __name__ == "__main__":
    pytest.main()