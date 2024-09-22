Traceback (most recent call last):
  File "/home/c0d3y/dev/JarvisV2/V2/JarvisV2.py", line 93, in <module>
    jarvis()  # Start the conversation
    ^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/V2/JarvisV2.py", line 75, in jarvis
    ai_response = model.invoke(user_input,session_id="1", language="english")
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/V2/ai_serviceV2.py", line 47, in invoke
    response = with_message_history.invoke(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 5343, in invoke
    return self.bound.invoke(
           ^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 5343, in invoke
    return self.bound.invoke(
           ^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 3022, in invoke
    input = context.run(step.invoke, input, config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 5343, in invoke
    return self.bound.invoke(
           ^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 4706, in invoke
    return self._call_with_config(
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 1923, in _call_with_config
    context.run(
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/config.py", line 396, in call_func_with_variable_args
    return func(input, **kwargs)  # type: ignore[call-arg]
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 4572, in _invoke
    output = output.invoke(
             ^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 5343, in invoke
    return self.bound.invoke(
           ^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/runnables/base.py", line 3022, in invoke
    input = context.run(step.invoke, input, config)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/language_models/llms.py", line 387, in invoke
    self.generate_prompt(
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/language_models/llms.py", line 752, in generate_prompt
    return self.generate(prompt_strings, stop=stop, callbacks=callbacks, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/language_models/llms.py", line 946, in generate
    output = self._generate_helper(
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/language_models/llms.py", line 789, in _generate_helper
    raise e
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_core/language_models/llms.py", line 776, in _generate_helper
    self._generate(
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_community/llms/ollama.py", line 431, in _generate
    final_chunk = super()._stream_with_aggregation(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_community/llms/ollama.py", line 348, in _stream_with_aggregation
    for stream_resp in self._create_generate_stream(prompt, stop, **kwargs):
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_community/llms/ollama.py", line 193, in _create_generate_stream
    yield from self._create_stream(
               ^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/langchain_community/llms/ollama.py", line 272, in _create_stream
    raise ValueError(
ValueError: Ollama call failed with status code 500. Details: {"error":"error loading model /usr/share/ollama/.ollama/models/blobs/sha256:633fc5be925f9a484b61d6f9b9a78021eeb462100bd557309f01ba84cac26"}