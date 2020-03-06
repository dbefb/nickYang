import coverage
cov = coverage.Coverage()
cov.start()

import test_caculator
test_caculator.main()

cov.stop()
cov.save()
cov.html_report(directory='F:/multisim/VsCode/软件工程学习/计算器单元测试、覆盖率测试/计算器覆盖率报告')