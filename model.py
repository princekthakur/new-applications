import xgboost as xgb
from sklearn.metrics import mean_squared_error

def train_model(X_train, y_train):
    model = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=100,
        learning_rate=0.1
    )
    model.fit(X_train, y_train)
    return model

# Example usage
# model = train_model(X_train, y_train)
# y_pred = model.predict(X_test)
# rmse = np.sqrt(mean_squared_error(y_test, y_pred))
