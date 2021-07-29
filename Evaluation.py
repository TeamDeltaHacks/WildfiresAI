
from Model import ObjectLocalizer
from PIL import Image , ImageDraw
import numpy as np

input_dim = 228

def calculate_avg_iou( target_boxes , pred_boxes ):
    xA = np.maximum( target_boxes[ ... , 0], pred_boxes[ ... , 0] )
    yA = np.maximum( target_boxes[ ... , 1], pred_boxes[ ... , 1] )
    xB = np.minimum( target_boxes[ ... , 2], pred_boxes[ ... , 2] )
    yB = np.minimum( target_boxes[ ... , 3], pred_boxes[ ... , 3] )
    interArea = np.maximum(0.0, xB - xA ) * np.maximum(0.0, yB - yA )
    boxAArea = (target_boxes[ ... , 2] - target_boxes[ ... , 0]) * (target_boxes[ ... , 3] - target_boxes[ ... , 1])
    boxBArea = (pred_boxes[ ... , 2] - pred_boxes[ ... , 0]) * (pred_boxes[ ... , 3] - pred_boxes[ ... , 1])
    iou = interArea / ( boxAArea + boxBArea - interArea )
    return iou

def class_accuracy( target_classes , pred_classes ):
    target_classes = np.argmax( target_classes , axis=1 )
    pred_classes = np.argmax( pred_classes , axis=1 )
    return ( target_classes == pred_classes ).mean()

X = np.load( 'wildfire_processed_data/x.npy')
Y = np.load( 'wildfire_processed_data/y.npy')
test_X = np.load( 'wildfire_processed_data/test_x.npy')
test_Y = np.load( 'wildfire_processed_data/test_y.npy')

print( X.shape )
print( Y.shape )
print( test_X.shape )
print( test_Y.shape )

localizer = ObjectLocalizer( input_shape=( input_dim , input_dim , 3 ) )
localizer.load_model_weights( 'pretrained_weights/pretrained_weights.h5' )

target_boxes = test_Y * input_dim
pred = localizer.predict( test_X )
pred_boxes = pred[ ... , 0 : 4 ] * input_dim
pred_classes = pred[ ... , 4 : ]

iou_scores = calculate_avg_iou( target_boxes , pred_boxes )
print( 'Mean IOU score {}'.format( iou_scores.mean() ) )

print( 'Class Accuracy is {} %'.format( class_accuracy( test_Y[ ... , 4 : ] , pred_classes ) * 100 ))

boxes = localizer.predict( test_X )
for i in range( boxes.shape[0] ):
    b = boxes[ i , 0 : 4 ] * input_dim
    img = test_X[i] * 255
    source_img = Image.fromarray( img.astype( np.uint8 ) , 'RGB' )
    draw = ImageDraw.Draw( source_img )
    draw.rectangle( b , outline="black" )
    source_img.save( 'wildfire_inference_images/image_{}.png'.format( i + 1 ) , 'png' )