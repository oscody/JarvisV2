#!/usr/bin/env python3
"""
Test script to verify that all key packages are working in the virtual environment
"""

def test_imports():
    """Test importing all key packages"""
    try:
        # Import audioop patch first
        import audioop_patch
        print("✓ audioop_patch imported successfully")
        
        # Test core packages
        import pyaudio
        print("✓ PyAudio imported successfully")
        
        import openai
        print("✓ OpenAI imported successfully")
        
        import torch
        print("✓ PyTorch imported successfully")
        
        import faster_whisper
        print("✓ Faster Whisper imported successfully")
        
        import pygame
        print("✓ Pygame imported successfully")
        
        import sounddevice
        print("✓ SoundDevice imported successfully")
        
        import simpleaudio
        print("✓ SimpleAudio imported successfully")
        
        import playsound
        print("✓ Playsound imported successfully")
        
        import soundfile
        print("✓ SoundFile imported successfully")
        
        import pydub
        print("✓ PyDub imported successfully")
        
        import ollama
        print("✓ Ollama imported successfully")
        
        import elevenlabs
        print("✓ ElevenLabs imported successfully")
        
        from dotenv import load_dotenv
        print("✓ Python-dotenv imported successfully")
        
        print("\n🎉 All packages imported successfully! Virtual environment is working properly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    print("Testing JarvisV2 virtual environment...")
    print("=" * 50)
    success = test_imports()
    print("=" * 50)
    if success:
        print("✅ Environment setup complete!")
    else:
        print("❌ Environment setup failed!") 