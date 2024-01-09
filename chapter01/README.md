# 1. Install docker
Follow steps from https://docs.docker.com/engine/install/

# 2. Create docker network
docker network create dev-network

# 3. Create docker volume
docker volume create dev-mongodb

# 4. Create docker containers using existing volumes, env files and dev-network:
docker run -d --name dev-mongodb --network dev-network --env-file=dev-mongodb.env -v dev-mongodb:/data/db -p 27017:27017 --restart on-failure:5 mongo:latest

# 5. Connect to mongodb server:
mongosh --host 127.0.0.1:27017 -u admin -p
test> use admin

# 6. Create new user with roles root or specific roles:
switched to db admin
admin> db.createUser({ user: "dbadmin", pwd: "dbadminP@ssw0rd", roles: ["root"]})
admin> db.createUser({ user: "dbadmin", pwd: "dbadmin", roles: ["readWriteAnyDatabase", "dbAdminAnyDatabase", "clusterAdmin"] })
admin> db.changeUserPassword('dbadmin', 'newP@ssw0rd')