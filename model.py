import cv2
import numpy as np
import tensorflow as tf

MODEL_FILENAME = 'model.pb'
LABELS_FILENAME = 'labels.txt'

INPUT_TENSOR_NAME = 'image_tensor:0'
OUTPUT_TENSOR_NAMES = ['detected_boxes:0', 'detected_scores:0', 'detected_classes:0']

### INIT
graph_def = tf.compat.v1.GraphDef()
with open(MODEL_FILENAME, 'rb') as f:
    graph_def.ParseFromString(f.read())

graph=tf.Graph()

with graph.as_default():
    tf.import_graph_def(graph_def, name='')

with tf.compat.v1.Session(graph=graph) as sess:
    input_shape = sess.graph.get_tensor_by_name(INPUT_TENSOR_NAME).shape.as_list()[1:3]

### INITIALIZE
with open(LABELS_FILENAME) as f:
    labels = [l.strip() for l in f.readlines()]

width = 320
height = 320

#initialize()

def predict(frame):
    with tf.compat.v1.Session(graph=graph) as sess:
        output_tensors = [sess.graph.get_tensor_by_name(n) for n in OUTPUT_TENSOR_NAMES]
        inp = cv2.resize(frame, (width, height))
        rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)
        inputs = np.array(rgb, dtype=np.float32)[np.newaxis, :, :, :]
        outputs = sess.run(output_tensors, {INPUT_TENSOR_NAME: inputs})
        predictions = [{'probability': round(float(p[1]), 8),
                        'tagId': int(p[2]),
                        'tagName': labels[p[2]],
                        'boundingBox': {
                            'left': round(float(p[0][0]), 8),
                            'top': round(float(p[0][1]), 8),
                            'width': round(float(p[0][2] - p[0][0]), 8),
                            'height': round(float(p[0][3] - p[0][1]), 8)
                        }
                    } for p in zip(*outputs)]
        return predictions
