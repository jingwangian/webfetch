#!/usr/bin/env python3
import os
import sys
import pytest

# print("current path:", os.getcwd())

# print(sys.path)


from webfetch.pipelines import WebfetchPipeline

file_name_1 = "tests/data/a1.html"


class TestWebfetchPipeline:
    def test_get_plain_text(self):
        wfp = WebfetchPipeline()

        with open(file_name_1, "rb") as f:
            # print(f.read())
            text = wfp.get_plain_text("http://a/b/c", f.read())
            # text = "abc"
            # text = f.read()

            print(text)

        assert 0
