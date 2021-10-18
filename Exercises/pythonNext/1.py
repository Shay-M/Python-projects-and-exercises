def scale_fit_transform(train_set, fictive_attr_name):
    # YOUR CODE HERE
    trained_scaling_info = pd.DataFrame([train_set.mean(), train_set.std()]).T
    info.columns = ['mean', 'std']
    mean = trained_scaling_info['mean']
    std = trained_scaling_info['std']

    train_set_scaled = (train_set - mean) / std

    return trained_scaling_info, train_set_scaled