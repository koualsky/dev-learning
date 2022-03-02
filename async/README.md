# Async usage
Don't think about async functions like on returning smthing by some endpoint.
But for example, like on scrapping websites. I ask some website about something, and I dont wait for response, but I made another request, and also I don't waint for response but made another one request. And responses will spływać do mnie niezależnie. I can describe how many tasks in one time I can have :)

That "wait for something else" normally refers to I/O operations that are relatively "slow" (compared to the speed of the processor and the RAM memory), like waiting for:

- the data from the client to be sent through the network
- the data sent by your program to be received by the client through the network
- the contents of a file in the disk to be read by the system and given to your program
- the contents your program gave to the system to be written to disk
- a remote API operation
- a database operation to finish
- a database query to return the results
- etc.

# Description
You can only use await inside of functions created with async def, like:
async def read_results():
    results = await some_library()
    return results

And if we want to made a few working tasks in one time, we should define few async def with await.
Then we can call these async functions in one time.

SO
If we define some function with async (async def ...), we have to use this function with await (res = await function()).
And if we will use this operation in some function, this function also should be define with async.

# Uvicorn
how to run app and describe amount of workers?
uvicorn file:app -w 4 --reload