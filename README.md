# Python-Signal-Processing
A college assignment where a frequency analysis had to be performed using the Fast Fourier Transform, a exemplary algorithm used in Digital Signal Processing

## Modules/Packages used:
<ol>
  <li>Scipy.fft</li>
  <li>Scipy.io.wavfile</li>
  <li>Numpy</li>
  <li>Matplotlib.pyplot</li>
</ol>

## Assignment Details:
Generate 2 sine waves.<br>
Synthesize the waves together.<br>
Transform using FFT to read frequency data.<br>
Analyze and remove a desired synthesized frequency.<br>
Normalize audio and save clean sine wave file.<br>

## Thorough Explanation:
Generate 2 sine waves, each from different frequencies. In this assignment: 432Hz and the other 4000Hz.<br>
Synthesize waves together and create a more complex sine wave. Once synthesized, a normalization had to take place.<br>
When normalized the audio has the ability to be visualized within the time domain and be saved locally as a .wav file.<br>
The following step, transform the audio to the frequency domain using the FFT algorithm.<br>
Once data has been transformed, another visualization can be done and see the 2 given frequencies on the graph.<br>
Analyze the frequency data and remove the desired frequency.<br>
Once desired frequency is removed, the data has to be transformed/reverted back into the time domain.<br>
Again the data has the ability to be visualized, this time if graphed, you will only notice the none-removed sine wave.<br>
When audio is finally transformed back into time domain, the audio is normalized ready to be played using an audio player.<br>
