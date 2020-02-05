#Author:Xiao Jian

import pytest

if __name__ == "__main__":

    pytest.main(["-m","smoke","--html","HtmlReport/report.html","--junitxml","HtmlReport/report.xml"])
