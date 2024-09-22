(JarvisV2) c0d3y@raspberrypi:~/dev/JarvisV2 $ python tests/3.ai/langchain_test.py 
Traceback (most recent call last):
  File "/home/c0d3y/dev/JarvisV2/tests/3.ai/langchain_test.py", line 21, in <module>
    result = chain.invoke({"input": "tell me about canada?"})
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
(JarvisV2) c0d3y@raspberrypi:~/dev/JarvisV2 $ 