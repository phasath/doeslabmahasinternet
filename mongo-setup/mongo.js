var db = connect('127.0.0.1:27017/labma');

db.createUser({
    user: "labmainternet",
    pwd: "labMA1nt4rnet!!",
    roles: [{
        role: "readWrite",
        db: "labma"
    }, {
        role: "dbOwner",
        db: "labma"
    }],
    mechanisms:[  
        "SCRAM-SHA-1"
    ]
});

db.createCollection('labma');