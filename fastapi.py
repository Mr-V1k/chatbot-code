from fastapi import FastAPI

@app.get("/parent/{query}")
async def parent(query: str, current_user: UserDetailsDB = Depends(get_current_active_user)):
    if current_user.disabled:
        return {"Error": "User is disabled. Contact Admin"}

    response = conversational_chat_parent(query, current_user.chat_history_parent)
    current_user.chat_history_parent = current_user.chat_history_parent + [{
        "Parent": query}, {"KiddyPi Chatbot": response}]

    session.commit()
    return {"KiddyPi Chatbot": response}
