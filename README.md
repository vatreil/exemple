
# Exemple



## API Reference

#### front

```django
  GET /user/user_name/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user_name` | `string` | **Required**. Url front |

#### backend

```flask
  GET /user/?user_name=user_name/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `user_name` | `string` | **Required**. Your API key |


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `URL_BACKEND` | `string` | http://127.0.0.1:5000 |

