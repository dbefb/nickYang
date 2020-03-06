import coverage
cov = coverage.Coverage()
cov.start()

import test_game_map
test_game_map.main()

cov.stop()
cov.save()
cov.html_report(directory='F:/multisim/VsCode/软件工程学习/覆盖率测试')