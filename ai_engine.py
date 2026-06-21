def get_ai_response(model, df, user_prompt):
    # Pass a sample of the data to the AI
    data_summary = df.head(15).to_string() 
    
    system_instruction = f"""
    You are an expert data analyst. Use the following dataset sample to answer questions:
    {data_summary}
    
    If you cannot answer from the data, state that clearly.
    """
    
    full_prompt = f"{system_instruction}\n\nUser Question: {user_prompt}"
    
    response = model.generate_content(full_prompt)
    return response.text