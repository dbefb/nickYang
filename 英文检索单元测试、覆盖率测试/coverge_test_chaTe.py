import coverage
cov = coverage.Coverage()
cov.start()

import test_ChapterTwoEX
test_ChapterTwoEX.main()

cov.stop()
cov.save()
cov.html_report(directory='F:/multisim/VsCode/软件工程学习/英文检索单元测试、覆盖率测试/覆盖率报告')