import React from 'react'

function Page({user}) {
    return (
        <div>
            <div>Page content: </div>
            <UserInfoWithTitle title='User Info' user={user} />
        </div>
    );
}

function UserInfoWithTitle({title, user}) {
    return (
        <div>
            <h1>{title}</h1>
            <UserInfo user={user}/>
        </div>
    )
}

function UserInfo({user}) {
    return (
        <div>
            <p>Name: {user.firstName} {user.lastName}</p>
        </div>
    )
}

export function Preview(){
    return (
        <Page user={{firstName: 'John', lastName: 'Doe'}} />
    )
}

export {
    Page,
    UserInfoWithTitle,
    UserInfo
}