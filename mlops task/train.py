import click



@click.command()
@click.option("--train-data", required=True, help="Path to the training data CSV file")
@click.option(
    "--train-labels", required=True, help="Path to the training labels CSV file"
)
@click.option(
    "--onnx-output", default="model/model.onnx", help="Path to save the ONNX model"
)
def main(train_data, train_labels, onnx_output):
    """
    Trains a classifier on the provided training data and labels, 
    and exports the trained model to ONNX format.

    Args:
        train_data (str): Path to the CSV file containing training features.
        train_labels (str): Path to the CSV file containing training labels.
        onnx_output (str): Path where the ONNX model will be saved.

    The function performs the following steps:
        1. Loads training features and labels from CSV files.
        2. If needed, runs preprocessing on the features.
        3. Trains a ML classifier.
        4. Converts the trained model to ONNX format and saves it to the specified path.
    """
    # [ADD] Load training data, run training, and export to ONNX
    
    with open(onnx_output, "wb") as f:
        f.write(onnx_model.SerializeToString())
    print(f"Model saved to {onnx_output}")


if __name__ == "__main__":
    main()
