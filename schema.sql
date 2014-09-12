drop table if exists entries;

PRAGMA foreign_keys = ON;

create table entries (
  eid integer primary key autoincrement,
  title text not null,
  text text not null
);

create table users (
  usid integer primary key autoincrement,
  username text not null,
  password text not null,
  email text not null,
  birthdate text not null,
  location text not null,
  quote text,
  postcount integer not null,
  joindate DATETIME DEFAULT CURRENT_TIMESTAMP not null
);

create table post (
  pid integer primary key autoincrement,
  authorid integer not null, 
  threadid integer not null,  
  postdate DATETIME DEFAULT CURRENT_TIMESTAMP not null,
  postcounter integer not null,
  content text not null,
  FOREIGN KEY(authorid) REFERENCES users,
  FOREIGN KEY(threadid) REFERENCES thread
);

create table thread (
  tid integer primary key autoincrement,
  title text not null,
  postdate DATETIME DEFAULT CURRENT_TIMESTAMP not null,
  authorid integer not null,
  visits integer not null,
  FOREIGN KEY(authorid) REFERENCES users
);

INSERT INTO users (username, password, email, location, birthdate, postcount) VALUES ("radu", "sturzu", "raduneo@gmail.com", "Montreal", "88-10-30", 0);

INSERT INTO thread (title, authorid, visits) VALUES ("Radu's great thread", last_insert_rowid(), 0);
INSERT INTO thread (title, authorid, visits) VALUES ("Radu's lonely thread", 1, 0);
INSERT INTO thread (title, authorid, visits) VALUES ("Radu's spicy thread", 1, 0);
INSERT INTO thread (title, authorid, visits) VALUES ("some random thread", 1, 0);

INSERT INTO post (threadid,authorid,content,postcounter) values (1, 1, "This is my first real post.. well it is clearly boring but let's see <strong>LET'S</strong> see!", 1)


  