from celery.utils.log import get_task_logger
from async_celery.app import app
import matplotlib.pyplot as plt
from PIL import Image

logger = get_task_logger(__name__)

@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True,
)
def plot_image_map(image_map_dimensions, image_map_data, results_size, generated_images_path):
    logger.info('Plotting image map Started')
    fig = plt.figure(figsize=(image_map_dimensions * 4.6, image_map_dimensions * 4.6))
    for i in range(0, len(image_map_data)):
        fig, ax = plt.subplots()
        ax.imshow(Image.fromarray(image_map_data['image'][i][0]).resize((results_size, results_size)), interpolation='nearest')
        ax.set_xticklabels([])
        ax.axes.get_xaxis().set_visible(False)
        ax.set_yticklabels([])
        ax.axes.get_yaxis().set_visible(False)
        # plt.show()
        plt.savefig(generated_images_path + '/{}.png'.format(image_map_data['name'][i]),bbox_inches = 'tight',pad_inches=0)
    logger.info('Plotting image map Completed')
    return {"status": "success", "message": "Image Created Successfully"}