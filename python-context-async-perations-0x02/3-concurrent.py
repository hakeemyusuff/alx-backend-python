import asyncio

import aiosqlite

async def async_fetch_users():
    connection = await aiosqlite.connect("users.db")
    cursor = await connection.execute("SELECT * FROM users")
    rows = await cursor.fetchall()
    await cursor.close()
    await connection.close()
    return  rows

async def async_fetch_older_users():
    connection = await aiosqlite.connect("users.db")
    cursor = await connection.execute("SELECT * FROM users WHERE age > ?", (40,))
    rows = await cursor.fetchall()
    await cursor.close()
    await connection.close()
    return  rows

async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

    print("All users: ", users)
    print("Users older than 40: ", older_users)

asyncio.run(fetch_concurrently())