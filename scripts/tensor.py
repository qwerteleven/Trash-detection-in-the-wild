import tensorflow
import tensorboard
from tensorboard import program
tracking_address = "/home/leopoldo/Escritorio/events"

tb = program.TensorBoard()

tb.configure(argv=[None, '--logdir', tracking_address])
url = tb.launch()
