from video2x.tests.test_upscaler import test_upscaling

import time

st = time.time()
test_upscaling(input_url=r'upload/2023-07-03-140109sea.mp4', output_url=r'output/2023-07-03-140109sea.mp4')
print(f'running time: {time.time() - st}')

# 17103.15162587166 (2, 8K)
# 4100.953718185425 (2, 4K)
# 1101.1094703674316 (2, x2)
# 1262.8228130340576 (2, x2) realcugan
#