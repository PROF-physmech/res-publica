create table user_roles (
        user_role_id            serial primary key,
        user_role_description   varchar(20) not null
);

create table users (
        user_id                 serial primary key,
        user_role               integer references user_roles(user_role_id) not null,
        user_name               varchar(200) not null,
        user_login              varchar(200),
        user_pass               varchar(200) not null,
        user_language_id 		varchar(5) references user_languages(user_language_id) not null,
        user_photo_id           varchar(100)
);

create table user_commentaries (
        user_commentary_id      serial primary key,
        user_commentary_data_id integer references commentries(commentary_id) not null,
        user_commentary_date    timestamp default now() not null,
        user_commentary_author  integer references users(user_id) not null,
        user_commented          integer references users(user_id) not null
);

create table conferences (
        conference_id           serial primary key,
        conference_name         varchar(100) not null,
        conference_description  varchar(500),
        conference_date         date not null,
        conference_start        time not null,
        conference_end          time not null
);

create table conferences_commentaries (
        conference_commentary_id        serial primary key,
        conference_commentary_data_id 	integer references commentries(commentary_id) not null,
        conference_commentary_date      timestamp default now() not null,
        conference_commentary_author    integer references users(user_id) not null,
        conference_commented            integer references conferences(conference_id) not null
);

create table presiding (
        presiding_id                    serial primary key,
        presiding_conference_id         integer references conferences(conference_id) not null,
        presiding_user_id               integer references users(user_id) not null
);

create table presiding_commentaries (
        presiding_commentary_id         serial primary key,
        presiding_commentary_data_id 	integer references commentries(commentary_id) not null,
        presiding_commentary_date       timestamp default now() not null,
        presiding_commentary_author     integer references users(user_id) not null,
        presiding_commented             integer references presiding(presiding_id) not null
);

create table delegates (
        delegate_id                     serial primary key,
        delegate_conference_id          integer references conferences(conference_id) not null,
        delegate_user_id                integer references users(user_id) not null
);

create table delegate_commentaries (
        delegate_commentary_id          serial primary key,
        delegate_commentary_data_id 	integer references commentries(commentary_id) not null,
        delegate_commentary_date        timestamp default now() not null,
        delegate_commentary_author      integer references users(user_id) not null,
        delegate_commented              integer references delegates(delegate_id) not null
);

create table votings (
        voting_id               serial primary key,
        voting_presiding_id     integer references presiding(presiding_id) not null,
        voting_statement        varchar(500) not null,
        voting_type             boolean not null,
        voting_start            time not null,
        voting_end              time not null
);

create table answers (
        answer_id               serial primary key,
        answer_voting_id        integer references votings(voting_id) not null,
        answer_statement        varchar(500) not null,
        answer_quantity         integer default 0 not null
);


create table votes (
        vote_id                 serial primary key,
        vote_answer_id          integer references answers(answer_id) not null,
        vote_delegates_id       integer references delegates(delegate_id) not null
);

create table commentries (
        commentary_id           serial primary key,
        commentary_text         varchar(500)
);

create table user_languages (
        user_language_id                varchar(5) primary key,
        user_language_description       varchar(100)
);
