import unittest
import os
from src.getGitURLS_UpdateClone_Submodule import get_git_urls


class TestGetGitUrls(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_dir'
        os.mkdir(self.test_dir)
        os.mkdir(os.path.join(self.test_dir, 'subdir'))
        with open(os.path.join(self.test_dir, '.git'), 'w') as f:
            f.write('url = https://github.com/test/repo.git')
        with open(os.path.join(self.test_dir, 'subdir', '.git'), 'w') as f:
            f.write('url = https://github.com/test/subrepo.git')

    def tearDown(self):
        os.remove(os.path.join(self.test_dir, '.git'))
        os.remove(os.path.join(self.test_dir, 'subdir', '.git'))
        os.rmdir(os.path.join(self.test_dir, 'subdir'))
        os.rmdir(self.test_dir)

    def test_get_git_urls(self):
        urls = get_git_urls(self.test_dir)
        self.assertEqual(len(urls), 2)
        self.assertIn('https://github.com/test/repo.git', urls)
        self.assertIn('https://github.com/test/subrepo.git', urls)
        

if __name__ == '__main__':
    unittest.main()