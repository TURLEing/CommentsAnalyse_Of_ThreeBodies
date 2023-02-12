from bilibili_api import bangumi, sync
from bilibili_api import settings
import numpy as np 

async def main():
    b = bangumi.Bangumi(897)
    next = None
    step = 0
    cmts = []
    cmt_X = np.array([])
    cmt_y = np.array([])
    while next != 0:
        print("Crawling at", step)
        step = step + 1
        cm = await b.get_short_comment_list(next=next)
        cmts.extend(cm['list'])
        next = cm['next']

    for cmt in cmts:
        cmt_X = np.append(cmt_X, cmt['content'])
        cmt_y = np.append(cmt_y, cmt['score'])
    
    return cmt_X, cmt_y

X, y = sync(main())
print
print(np.sum(y>8))

