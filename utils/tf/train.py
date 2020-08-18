import tensorflow as tf
from tensorflow.python.keras.utils.generic_utils import to_list


def train_step(model, optimizer, f_loss, x_train, y_train):
    """Training step for a model.
    """
    with tf.GradientTape() as tape:
        predictions = to_list(model(x_train, training=True))
        loss = f_loss(y_train, predictions)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return loss


def f_callback_basic(epoch, loss, *args, **kwargs):
    if epoch%100==0:
        tf.print("Epoch: {}\tLoss: {}".format(epoch,loss))


def train(model, f_loss, optimizer, batch_size, epochs, x_train, y_train, f_callback=f_callback_basic):
    """Train a model with stochastic gradient descent.
    """

    len_dataset = len(x_train[0])
    indices = tf.range(len_dataset) # All indices for the dataset samples

    for epoch in range(epochs):
        indices = tf.random.shuffle(indices)
        i_batch = 0
        while i_batch<len_dataset:
            batch_indices = indices[i_batch:i_batch+batch_size]  # Stochastic batch selection
            loss = train_step(
                model,
                optimizer,
                f_loss,
                x_train=[
                    tf.gather(params=feat_x, indices=batch_indices)
                    for feat_x in x_train
                ],
                y_train=[
                    tf.gather(params=feat_y, indices=batch_indices)
                    for feat_y in y_train
                ],
            )
            i_batch += batch_size
        if f_callback:
            f_callback(epoch, loss, model)

