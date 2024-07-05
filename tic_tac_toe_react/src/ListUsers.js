import React from 'react'

const ListUsers = ({users = []}) => {
    const userCount = users.length;

    if(userCount === 0) {
        return (
            <div>
                <h2>Users List</h2>
                <p>Total users: 0</p>
            </div>
        )
    }

    const sortedUsers = users.sort((a, b) => {
        const lastNameA = a.lastName.toLowerCase();
        const lastNameB = b.lastName.toLowerCase();
        if (lastNameA < lastNameB) {
          return -1;
        }
        if (lastNameA > lastNameB) {
          return 1;
        }
        return 0;
      });

  return (
    <>
    <h2>Users List</h2>
    <p>Total Users: {userCount}</p>
    <div className="user-count">
        Users: {userCount}
    </div>
    <ul className="user-list">
        {sortedUsers.map((user) => (
            <li key={user.lastName}>
                {user.firstName} {user.lastName}
            </li>
        ))}
    </ul>
    </>
  )
}

export default ListUsers