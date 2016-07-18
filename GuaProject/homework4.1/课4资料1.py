# 2016/7/15
#
# ========
# 课 4 的资料
# 关于模块和 import
# ========
#


# import 之后就可以使用
# 这样的方式可以引用 utils 模块内的所有名字
import utils
# 但是注意, 必须加上模块名字使用
# 所以是 utils.log 而不是 log
utils.log('import 的 log 函数')
utils.log('变量也可以被 import', utils.pi)


# 可以在 import 的时候给模块改名
import utils as gsju
# 现在用新名字 gsju 引用 utils 模块了
gsju.log('模块也能改名')
gsju.log('改名模块引用其他名字', gsju.pi)
gsju.log('debug', gsju.__name__)


# 可以通过 from import 语法直接引入名字
# 但是这样只引入了一个 log
# pi 是没有被引入的
from utils import log
# 这样引入的话, 就能直接使用 log 函数
log('直接使用 log')


# 可以给 import 进来的东西改名字
from utils import pi as pie
# 现在就可以通过 pie 来得到 utils.pi 的值了
print('改名', pie)
