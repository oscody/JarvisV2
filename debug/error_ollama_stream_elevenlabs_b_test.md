




(JarvisV2) (base) bogle@Bogles-MacBook-Pro JarvisV2 % python tests/3.ai/ollama_stream_elevenlabs_b_test.py


/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_config.py:334: UserWarning: Valid config keys have changed in V2:
* 'allow_population_by_field_name' has been renamed to 'populate_by_name'
* 'smart_union' has been removed
  warnings.warn(message, UserWarning)
/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_fields.py:160: UserWarning: Field "model_id" has conflict with protected namespace "model_".

You may be able to resolve this warning by setting `model_config['protected_namespaces'] = ()`.
  warnings.warn(
Traceback (most recent call last):
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_b_test.py", line 26, in <module>
    messages = [{"role": "system", "content": systaem_message}, {"role": "user", "content": user_input}]
                                              ^^^^^^^^^^^^^^^
NameError: name 'systaem_message' is not defined. Did you mean: 'system_message'?
(JarvisV2) (base) bogle@Bogles-MacBook-Pro JarvisV2 % python tests/3.ai/ollama_stream_elevenlabs_b_test.py
/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_config.py:334: UserWarning: Valid config keys have changed in V2:
* 'allow_population_by_field_name' has been renamed to 'populate_by_name'
* 'smart_union' has been removed
  warnings.warn(message, UserWarning)
/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_fields.py:160: UserWarning: Field "model_id" has conflict with protected namespace "model_".

You may be able to resolve this warning by setting `model_config['protected_namespaces'] = ()`.
  warnings.warn(
Traceback (most recent call last):
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_b_test.py", line 51, in <module>
    stream(audio_stream)
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/elevenlabs/play.py", line 76, in stream
    raise ValueError(message)
ValueError: mpv not found, necessary to stream audio. On mac you can install it with 'brew install mpv'. On linux and windows you can install it from https://mpv.io/



(JarvisV2) (base) bogle@Bogles-MacBook-Pro JarvisV2 % brew install mpv
==> Auto-updating Homebrew...
Adjust how often this is run with HOMEBREW_AUTO_UPDATE_SECS or disable with
HOMEBREW_NO_AUTO_UPDATE. Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Downloading https://ghcr.io/v2/homebrew/portable-ruby/portable-ruby/blobs/sha256:ce5c135bf98da783bf5964e89aab587e3341c8adc379f36ace17ae7881f53e8c
###################################################################################################################### 100.0%
==> Pouring portable-ruby-3.3.4_1.arm64_big_sur.bottle.tar.gz
==> Auto-updated Homebrew!
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
aider             kubehound         libgedit-gfls     mysql-client@8.4  onion-location    progressline      tabiew
clangql           libassuan@2       libxpresent       mysql@8.4         oxker             sq                usage
==> New Casks
find-my-ports                  meta-quest-developer-hub       pearcleaner                    zipic

You have 18 outdated formulae and 2 outdated casks installed.

Warning: Treating mpv as a formula. For the cask, use homebrew/cask/stolendata-mpv or specify the `--cask` flag.
==> Downloading https://ghcr.io/v2/homebrew/core/mpv/manifests/0.38.0_2-1
###################################################################################################################### 100.0%
==> Fetching dependencies for mpv: libx11, sdl2, ffmpeg, shaderc, vulkan-headers, vulkan-loader, libplacebo, luajit, mujs, uchardet, vapoursynth, certifi, yt-dlp and molten-vk
==> Downloading https://ghcr.io/v2/homebrew/core/libx11/manifests/1.8.10
###################################################################################################################### 100.0%
==> Fetching libx11
==> Downloading https://ghcr.io/v2/homebrew/core/libx11/blobs/sha256:5467d41501260e483586e9b05ed3137393f7faf7d49901c31bbeb0b2
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sdl2/manifests/2.30.6
###################################################################################################################### 100.0%
==> Fetching sdl2
==> Downloading https://ghcr.io/v2/homebrew/core/sdl2/blobs/sha256:c88013f3dacc2dedcc4972954127b1ae90c1216da12a3da273ac1647eb
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/ffmpeg/manifests/7.0.2
###################################################################################################################### 100.0%
==> Fetching ffmpeg
==> Downloading https://ghcr.io/v2/homebrew/core/ffmpeg/blobs/sha256:12453b675bcd28141bd0d477b74632ce63978ce479b12b608d73c8e6
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/shaderc/manifests/2024.0
###################################################################################################################### 100.0%
==> Fetching shaderc
==> Downloading https://ghcr.io/v2/homebrew/core/shaderc/blobs/sha256:9e91b9ca535fd4f4251290a9f05aab1d3714ddcff8a64e7f1fad846
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-headers/manifests/1.3.292
###################################################################################################################### 100.0%
==> Fetching vulkan-headers
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-headers/blobs/sha256:81dae8b70585fd03fd314b7b582945fc7160d8761a7fa673
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-loader/manifests/1.3.292
###################################################################################################################### 100.0%
==> Fetching vulkan-loader
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-loader/blobs/sha256:686ad04e1c064a0bf679d80525fd5d66c48b72e53c3c742f5
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/libplacebo/manifests/7.349.0
###################################################################################################################### 100.0%
==> Fetching libplacebo
==> Downloading https://ghcr.io/v2/homebrew/core/libplacebo/blobs/sha256:72afc163cc9dfc5525ed856094449685f034dfbbd8528f04e448
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/luajit/manifests/2.1.1720049189
###################################################################################################################### 100.0%
==> Fetching luajit
==> Downloading https://ghcr.io/v2/homebrew/core/luajit/blobs/sha256:3bc6f2b267326017a3e879bdaf0a74ac47a47187de26b5315270f672
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/mujs/manifests/1.3.5
###################################################################################################################### 100.0%
==> Fetching mujs
==> Downloading https://ghcr.io/v2/homebrew/core/mujs/blobs/sha256:730e76d17786653ff4a36ce09f749b203b6883195f645fefb9958d413a
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/uchardet/manifests/0.0.8
###################################################################################################################### 100.0%
==> Fetching uchardet
==> Downloading https://ghcr.io/v2/homebrew/core/uchardet/blobs/sha256:70b2c779c315b71c067c8f4a743a90688dfa329c9d5e1c174345d0
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/vapoursynth/manifests/69
###################################################################################################################### 100.0%
==> Fetching vapoursynth
==> Downloading https://ghcr.io/v2/homebrew/core/vapoursynth/blobs/sha256:c068b4aae76a49f75fa69f2a0c912b2c42cae12e23633a62790
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/certifi/manifests/2024.7.4
###################################################################################################################### 100.0%
==> Fetching certifi
==> Downloading https://ghcr.io/v2/homebrew/core/certifi/blobs/sha256:4106d660c4417641c4384ee68ab6c4146da998c22da4798ff94b03a
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/yt-dlp/manifests/2024.8.1
###################################################################################################################### 100.0%
==> Fetching yt-dlp
==> Downloading https://ghcr.io/v2/homebrew/core/yt-dlp/blobs/sha256:712b15c634441a15fd3b612bdcab23538638a8af7091b5ea2d4444e0
###################################################################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/molten-vk/manifests/1.2.10
###################################################################################################################### 100.0%
==> Fetching molten-vk
==> Downloading https://ghcr.io/v2/homebrew/core/molten-vk/blobs/sha256:25a56ad433bb2d345a836eda1cc7063b7cac29e09f147e55cd3e1
###################################################################################################################### 100.0%
==> Fetching mpv
==> Downloading https://ghcr.io/v2/homebrew/core/mpv/blobs/sha256:4dbf5f21d142921fd15db9e065d9a8676c4a20c4970b38decc75a698aeb
###################################################################################################################### 100.0%
==> Installing dependencies for mpv: libx11, sdl2, ffmpeg, shaderc, vulkan-headers, vulkan-loader, libplacebo, luajit, mujs, uchardet, vapoursynth, certifi, yt-dlp and molten-vk
==> Installing mpv dependency: libx11
==> Downloading https://ghcr.io/v2/homebrew/core/libx11/manifests/1.8.10
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/2e75e14e6bb3157688933738ae64e0dc86954ca8ef075737dda6b890d605d566--libx11-1.8.10.bottle_manifest.json
==> Pouring libx11--1.8.10.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libx11/1.8.10: 1,043 files, 7MB
==> Installing mpv dependency: sdl2
==> Downloading https://ghcr.io/v2/homebrew/core/sdl2/manifests/2.30.6
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/081e7ac28d34a09f27a48c56e7d5f911655b7af9be71f00e0f74a182d6ab3af3--sdl2-2.30.6.bottle_manifest.json
==> Pouring sdl2--2.30.6.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/sdl2/2.30.6: 94 files, 6.5MB
==> Installing mpv dependency: ffmpeg
==> Downloading https://ghcr.io/v2/homebrew/core/ffmpeg/manifests/7.0.2
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/10c2f8b546f7363feeedaa9871effbafed1cfc028f6904942060c6ef18df51c6--ffmpeg-7.0.2.bottle_manifest.json
==> Pouring ffmpeg--7.0.2.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/ffmpeg/7.0.2: 287 files, 51.8MB
==> Installing mpv dependency: shaderc
==> Downloading https://ghcr.io/v2/homebrew/core/shaderc/manifests/2024.0
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/d62525a094d3a1aebd9db31302bfd6d85e7c270ebb5418e1776e4d3aaa9c68b9--shaderc-2024.0.bottle_manifest.json
==> Pouring shaderc--2024.0.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/shaderc/2024.0: 21 files, 28.8MB
==> Installing mpv dependency: vulkan-headers
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-headers/manifests/1.3.292
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/ea6254dc90c1ac2816a12d73155f31b03ec73a8d359f4e39f39893098a3100b8--vulkan-headers-1.3.292.bottle_manifest.json
==> Pouring vulkan-headers--1.3.292.all.bottle.tar.gz
🍺  /opt/homebrew/Cellar/vulkan-headers/1.3.292: 64 files, 26.1MB
==> Installing mpv dependency: vulkan-loader
==> Downloading https://ghcr.io/v2/homebrew/core/vulkan-loader/manifests/1.3.292
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/e0e42257ec207577ebcc6f777fd5b79665d6d5a2c9f4a0b40fb01613c0666c93--vulkan-loader-1.3.292.bottle_manifest.json
==> Pouring vulkan-loader--1.3.292.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/vulkan-loader/1.3.292: 16 files, 1.1MB
==> Installing mpv dependency: libplacebo
==> Downloading https://ghcr.io/v2/homebrew/core/libplacebo/manifests/7.349.0
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/78e87199bbe70955838d4d0d125af2e4c7d863df0b8e7613277396bd7b6460d0--libplacebo-7.349.0.bottle_manifest.json
==> Pouring libplacebo--7.349.0.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/libplacebo/7.349.0: 42 files, 1.4MB
==> Installing mpv dependency: luajit
==> Downloading https://ghcr.io/v2/homebrew/core/luajit/manifests/2.1.1720049189
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/d8490c3f3ae534301b5f662fe61889cd038589c56479b9c78a456b5ba7e92d79--luajit-2.1.1720049189.bottle_manifest.json
==> Pouring luajit--2.1.1720049189.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/luajit/2.1.1720049189: 56 files, 2.1MB
==> Installing mpv dependency: mujs
==> Downloading https://ghcr.io/v2/homebrew/core/mujs/manifests/1.3.5
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/bb838e07c0f3437d909aee78347f0525f3e347392e7b2ff5db07368d4ecd0f95--mujs-1.3.5.bottle_manifest.json
==> Pouring mujs--1.3.5.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mujs/1.3.5: 12 files, 1.2MB
==> Installing mpv dependency: uchardet
==> Downloading https://ghcr.io/v2/homebrew/core/uchardet/manifests/0.0.8
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/37b3de4d13c09c3d82538e234ab5da0b279d7c244141bce073d16baa75b483a5--uchardet-0.0.8.bottle_manifest.json
==> Pouring uchardet--0.0.8.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/uchardet/0.0.8: 18 files, 657.0KB
==> Installing mpv dependency: vapoursynth
==> Downloading https://ghcr.io/v2/homebrew/core/vapoursynth/manifests/69
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/e8682b4b0685a14baa4ebb92fde7b5b4661d4a55be0ef799549003dd92549231--vapoursynth-69.bottle_manifest.json
==> Pouring vapoursynth--69.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/vapoursynth/69: 22 files, 3.6MB
==> Installing mpv dependency: certifi
==> Downloading https://ghcr.io/v2/homebrew/core/certifi/manifests/2024.7.4
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/5c48e1fedf564438f1080cc7bc12ed767674eb66d42d61715e4e991fdfe20ff4--certifi-2024.7.4.bottle_manifest.json
==> Pouring certifi--2024.7.4.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/certifi/2024.7.4: 27 files, 25.9KB
==> Installing mpv dependency: yt-dlp
==> Downloading https://ghcr.io/v2/homebrew/core/yt-dlp/manifests/2024.8.1
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/b052f2da30c997f1ac5bea2e5693c8fffbcbb84b2e1d589bc8b8794581d1a63c--yt-dlp-2024.8.1.bottle_manifest.json
==> Pouring yt-dlp--2024.8.1.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/yt-dlp/2024.8.1: 1,668 files, 18.3MB
==> Installing mpv dependency: molten-vk
==> Downloading https://ghcr.io/v2/homebrew/core/molten-vk/manifests/1.2.10
Already downloaded: /Users/bogle/Library/Caches/Homebrew/downloads/481afaadbaec98d953f7b0e9e1418cfd1ec0e27717789e6019e3465326fe7be5--molten-vk-1.2.10.bottle_manifest.json
==> Pouring molten-vk--1.2.10.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/molten-vk/1.2.10: 149 files, 91.8MB
==> Installing mpv
==> Pouring mpv--0.38.0_2.arm64_sonoma.bottle.1.tar.gz
==> Caveats
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions
==> Summary
🍺  /opt/homebrew/Cellar/mpv/0.38.0_2: 34 files, 9.3MB
==> Running `brew cleanup mpv`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> mpv
zsh completions have been installed to:
  /opt/homebrew/share/zsh/site-functions


(JarvisV2) (base) bogle@Bogles-MacBook-Pro JarvisV2 % python tests/3.ai/ollama_stream_elevenlabs_b_test.py

/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_config.py:334: UserWarning: Valid config keys have changed in V2:
* 'allow_population_by_field_name' has been renamed to 'populate_by_name'
* 'smart_union' has been removed
  warnings.warn(message, UserWarning)
/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/pydantic/_internal/_fields.py:160: UserWarning: Field "model_id" has conflict with protected namespace "model_".

You may be able to resolve this warning by setting `model_config['protected_namespaces'] = ()`.
  warnings.warn(
Response: Lou
Response: ise
Response:  Bor
Response: el
Response:  is
Response:  attributed
Response:  as
Response:  the
Response:  painter
Response:  of
Response:  Leon
Response: ardo
Response:  da
Response:  V
Response: inci
Response: '
Response: s
Response:  famous
Response:  Mon
Response: a
Response:  Lisa
Response: ,
Response:  also
Response:  known
Response:  as
Response:  La
Response:  G
Response: io
Response: conda
Response: .
Response:  However
Response: ,
Response:  there
Response:  are
Response:  several
Response:  theories
Response:  about
Response:  who
Response:  painted
Response:  the
Response:  painting
Response:  and
Response:  what
Response:  the
Response:  author
Response: '
Response: s
Response:  name
Response:  could
Response:  really
Response:  be
Response: .
Response:  Some
Response:  research
Response: ers
Response:  believe
Response:  the
Response:  actual
Response:  author
Response:  may
Response:  have
Response:  been
Response:  a
Response:  secret
Response:  ci
Response: pher
Response:  which
Response:  has
Response:  only
Response:  recently
Response:  started
Response:  to
Response:  reve
Response: al
Response:  itself
Response:  since
Response:  the
Response:  end
Response:  of
Response:  World
Traceback (most recent call last):
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/elevenlabs/realtime_tts.py", line 120, in convert_realtime
    socket.send(json.dumps(data))
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/websockets/sync/connection.py", line 284, in send
    with self.send_context():
  File "/opt/homebrew/Cellar/python@3.11/3.11.4/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/websockets/sync/connection.py", line 724, in send_context
    raise self.protocol.close_exc from original_exc
websockets.exceptions.ConnectionClosedError: received 1008 (policy violation) Unusual activity detected. Free Tier usage disabled. If you are using a proxy/VPN you might need to purchase a Paid Plan; then sent 1008 (policy violation) Unusual activity detected. Free Tier usage disabled. If you are using a proxy/VPN you might need to purchase a Paid Plan

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/bogle/Dev/Agent/JarvisV2/tests/3.ai/ollama_stream_elevenlabs_b_test.py", line 51, in <module>
    stream(audio_stream)
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/elevenlabs/play.py", line 88, in stream
    for chunk in audio_stream:
  File "/Users/bogle/Dev/Agent/JarvisV2/JarvisV2/lib/python3.11/site-packages/elevenlabs/realtime_tts.py", line 139, in convert_realtime
    raise ApiError(body=ce.reason, status_code=ce.code)
elevenlabs.core.api_error.ApiError: status_code: 1008, body: Unusual activity detected. Free Tier usage disabled. If you are using a proxy/VPN you might need to purchase a Paid Plan