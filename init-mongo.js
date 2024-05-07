db = db.getSiblingDB('flask');
db.createUser(
 {
   user: "flask",
   pwd: "flask",
   roles: [
    { role: "readWrite", db: "flask" }
   ]
 }
);