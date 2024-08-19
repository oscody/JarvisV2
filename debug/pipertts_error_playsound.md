(JarvisV2) c0d3y@raspberrypi:~/dev/JarvisV2 $ python tests/4.speak/pipertts_test_speed.py 
playsound is relying on another python subprocess. Please use `pip install pygobject` if you want playsound to run more efficiently.
Time taken to synthesize and write to file: 0.7588 seconds
Traceback (most recent call last):
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 261, in <module>
    playsound(argv[1])
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 163, in _playsoundNix
    gi.require_version('Gst', '1.0')
  File "/usr/lib/python3/dist-packages/gi/__init__.py", line 126, in require_version
    raise ValueError('Namespace %s not available' % namespace)
ValueError: Namespace Gst not available
Traceback (most recent call last):
  File "/home/c0d3y/dev/JarvisV2/tests/4.speak/pipertts_test_speed.py", line 43, in <module>
    playsound('Voice/pipertts.wav')
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 254, in <lambda>
    playsound = lambda sound, block = True: _playsoundAnotherPython('/usr/bin/python3', sound, block, macOS = False)
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 229, in _playsoundAnotherPython
    t.join()
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 218, in join
    raise self.exc
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 211, in run
    self.ret = self._target(*self._args, **self._kwargs)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py", line 226, in <lambda>
    t = PropogatingThread(target = lambda: check_call([otherPython, playsoundPath, _handlePathOSX(sound) if macOS else sound]))
                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/subprocess.py", line 413, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/usr/bin/python3', '/home/c0d3y/dev/JarvisV2/JarvisV2/lib/python3.11/site-packages/playsound.py', 'Voice/pipertts.wav']' returned non-zero exit status 1.
(JarvisV2) c0d3y@raspberrypi:~/dev/JarvisV2 $ pip install pygobject
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting pygobject
  Using cached pygobject-3.48.2.tar.gz (715 kB)
  Installing build dependencies ... error
  error: subprocess-exited-with-error
  
  × pip subprocess to install build dependencies did not run successfully.
  │ exit code: 1
  ╰─> [46 lines of output]
      Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple, https://www.piwheels.org/simple
      Collecting meson-python>=0.12.1
        Using cached https://www.piwheels.org/simple/meson-python/meson_python-0.16.0-py3-none-any.whl (26 kB)
      Collecting pycairo>=1.16
        Using cached pycairo-1.26.1.tar.gz (346 kB)
        Installing build dependencies: started
        Installing build dependencies: finished with status 'done'
        Getting requirements to build wheel: started
        Getting requirements to build wheel: finished with status 'done'
        Preparing metadata (pyproject.toml): started
        Preparing metadata (pyproject.toml): finished with status 'done'
      Collecting meson>=0.63.3
        Using cached https://www.piwheels.org/simple/meson/meson-1.5.1-py3-none-any.whl (960 kB)
      Collecting packaging>=19.0
        Using cached https://www.piwheels.org/simple/packaging/packaging-24.1-py3-none-any.whl (53 kB)
      Collecting pyproject-metadata>=0.7.1
        Using cached https://www.piwheels.org/simple/pyproject-metadata/pyproject_metadata-0.8.0-py3-none-any.whl (7.5 kB)
      Building wheels for collected packages: pycairo
        Building wheel for pycairo (pyproject.toml): started
        Building wheel for pycairo (pyproject.toml): finished with status 'error'
        error: subprocess-exited-with-error
      
        × Building wheel for pycairo (pyproject.toml) did not run successfully.
        │ exit code: 1
        ╰─> [15 lines of output]
            running bdist_wheel
            running build
            running build_py
            creating build
            creating build/lib.linux-aarch64-cpython-311
            creating build/lib.linux-aarch64-cpython-311/cairo
            copying cairo/__init__.py -> build/lib.linux-aarch64-cpython-311/cairo
            copying cairo/__init__.pyi -> build/lib.linux-aarch64-cpython-311/cairo
            copying cairo/py.typed -> build/lib.linux-aarch64-cpython-311/cairo
            running build_ext
            Package cairo was not found in the pkg-config search path.
            Perhaps you should add the directory containing `cairo.pc'
            to the PKG_CONFIG_PATH environment variable
            Package 'cairo', required by 'virtual:world', not found
            Command '['pkg-config', '--print-errors', '--exists', 'cairo >= 1.15.10']' returned non-zero exit status 1.
            [end of output]
      
        note: This error originates from a subprocess, and is likely not a problem with pip.
        ERROR: Failed building wheel for pycairo
      Failed to build pycairo
      ERROR: Could not build wheels for pycairo, which is required to install pyproject.toml-based projects
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× pip subprocess to install build dependencies did not run successfully.
│ exit code: 1
╰─> See above for output.



note: This error originates from a subprocess, and is likely not a problem with pip.
(JarvisV2) c0d3y@raspberrypi:~/dev/JarvisV2 $ 