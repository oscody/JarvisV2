


975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x140005f40] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x140005b30] Failed to find two consecutive MPEG audio frames.
[cache @ 0x140005f40] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x1400058e0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-224 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x14df22b40] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x14df227a0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x14df22b40] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x14df22550] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-225 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x11e7065e0] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x11e7061e0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x11e7065e0] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x11e705f90] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-226 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x146e2df80] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x146e2dbc0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x146e2df80] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x146e2d970] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-227 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x159706b90] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x1597067d0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x159706b90] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x159706580] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-228 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x148806030] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x148805c20] Failed to find two consecutive MPEG audio frames.
[cache @ 0x148806030] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x1488059d0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-229 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x14c62d510] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x14c62d150] Failed to find two consecutive MPEG audio frames.
[cache @ 0x14c62d510] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x14c62cf00] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-230 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x128f06030] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x128f05c20] Failed to find two consecutive MPEG audio frames.
[cache @ 0x128f06030] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x128f059d0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-231 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x135706030] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x135705c20] Failed to find two consecutive MPEG audio frames.
[cache @ 0x135706030] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x1357059d0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-232 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x12bf05f40] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x12bf05b30] Failed to find two consecutive MPEG audio frames.
[cache @ 0x12bf05f40] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x12bf058e0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-233 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x12262d4b0] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x12262d0f0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x12262d4b0] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x12262cea0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-234 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x11ce06170] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x11ce05d40] Failed to find two consecutive MPEG audio frames.
[cache @ 0x11ce06170] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x11ce05af0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-235 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x131e2d410] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x131e2d050] Failed to find two consecutive MPEG audio frames.
[cache @ 0x131e2d410] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x131e2ce00] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Exception in thread Thread-236 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x135f06a20] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x135f065f0] Failed to find two consecutive MPEG audio frames.
[cache @ 0x135f06a20] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x135f063a0] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input

Response: The painting of "The Lajoie Girl" by Leonardo da Vinci was first attributed to an unidentified painter for decades. In 2019, a team of scientists, including Professor Barbara Valdenegro of the University of Paris-Saclay who was then working with DaVinci's "Monotone Model," successfully analyzed polychromatic layers in this painting to determine that it is a painting by da Vinci.

The Mona Lisa was originally commissioned by the painter Francesco del Giocondo, commonly known as "da Vinci" in his honor. After da Vinci's death in 1519, his widow Maria Salutati sold the picture to King François I of France for 40,000 francs - worth approximately $2 million today. Many theories are offered about who painted this masterpiece, including Leonardo daVinci, but due to the numerous similarities in style and subject matter with the Mona Lisa, art historians settled on DaVinci's identity as the author of "The LaJoie Girl."
Time taken: 272.25 seconds
Exception in thread Thread-237 (play_audio_stream):
Traceback (most recent call last):
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_test.py", line 56, in play_audio_stream
    audio = AudioSegment.from_file(audio_stream, format="mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydub/audio_segment.py", line 773, in from_file
    raise CouldntDecodeError(
pydub.exceptions.CouldntDecodeError: Decoding failed. ffmpeg returned error code: 183

Output from ffmpeg/avlib:

ffmpeg version 7.0.1 Copyright (c) 2000-2024 the FFmpeg developers
  built with Apple clang version 15.0.0 (clang-1500.3.9.4)
  configuration: --prefix=/opt/homebrew/Cellar/ffmpeg/7.0.1 --enable-shared --enable-pthreads --enable-version3 --cc=clang --host-cflags= --host-ldflags='-Wl,-ld_classic' --enable-ffplay --enable-gnutls --enable-gpl --enable-libaom --enable-libaribb24 --enable-libbluray --enable-libdav1d --enable-libharfbuzz --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librav1e --enable-librist --enable-librubberband --enable-libsnappy --enable-libsrt --enable-libssh --enable-libsvtav1 --enable-libtesseract --enable-libtheora --enable-libvidstab --enable-libvmaf --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxml2 --enable-libxvid --enable-lzma --enable-libfontconfig --enable-libfreetype --enable-frei0r --enable-libass --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libspeex --enable-libsoxr --enable-libzmq --enable-libzimg --disable-libjack --disable-indev=jack --enable-videotoolbox --enable-audiotoolbox --enable-neon
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[cache @ 0x13b62d410] Inner protocol failed to seekback end : -78
    Last message repeated 1 times
[mp3 @ 0x13b62d050] Failed to find two consecutive MPEG audio frames.
[cache @ 0x13b62d410] Statistics, cache hits:0 cache misses:0
[in#0 @ 0x13b62ce00] Error opening input: Invalid data found when processing input
Error opening input file cache:pipe:0.
Error opening input files: Invalid data found when processing input