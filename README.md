# RestfulUnitTest
Flask app, Flask-Restful, unit test...
```
如果在create_app之前创建restful.Api()实例，那么在创建完app之后要:
1. api.app = app
2. api.init(app)
```
