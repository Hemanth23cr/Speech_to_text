# Speech_to_text

Have you ever wondered how to add speech recognition to your Python project? If so, then keep reading! It’s easier than you might think.

Far from a being a fad, the overwhelming success of speech-enabled products like Amazon Alexa has proven that some degree of speech support will be an essential aspect of household tech for the foreseeable future. If you think about it, the reasons why are pretty obvious. Incorporating speech recognition into your Python application offers a level of interactivity and accessibility that few technologies can match.

The accessibility improvements alone are worth considering. Speech recognition allows the elderly and the physically and visually impaired to interact with state-of-the-art products and services quickly and naturally—no GUI needed!

Best of all, including speech recognition in a Python project is really simple. In this guide, you’ll find out how. You’ll learn:

  * How speech recognition works.
    
  * How to install and use the SpeechRecognition package—a full-featured and easy-to-use Python speech recognition library.


<section class="section2" id="how-speech-recognition-works-an-overview"><h2>How Speech Recognition Works – An Overview</h2>
<p>Before we get to the nitty-gritty of doing speech recognition in Python, let’s take a moment to talk about how speech recognition works. A full discussion would fill a book, so I won’t bore you with all of the technical details here. In fact, this section is not pre-requisite to the rest of the tutorial. If you’d like to get straight to the point, then feel free to skip ahead.</p>
<p>Speech recognition has its roots in research done at Bell Labs in the early 1950s. Early systems were limited to a single speaker and had limited vocabularies of about a dozen words. Modern speech recognition systems have come a long way since their ancient counterparts. They can recognize speech from multiple speakers and have enormous vocabularies in numerous languages.</p>
<p>The first component of speech recognition is, of course, speech. Speech must be converted from physical sound to an electrical signal with a microphone, and then to digital data with an analog-to-digital converter. Once digitized, several models can be used to transcribe the audio to text.</p>
<p>Most modern speech recognition systems rely on what is known as a <a href="https://en.wikipedia.org/wiki/Hidden_Markov_model">Hidden Markov Model</a> (HMM). This approach works on the assumption that a speech signal, when viewed on a short enough timescale (say, ten milliseconds), can be reasonably approximated as a stationary process—that is, a process in which statistical properties do not change over time.</p>
<p>In a typical HMM, the speech signal is divided into 10-millisecond fragments. The power spectrum of each fragment, which is essentially a plot of the signal’s power as a function of frequency, is mapped to a vector of real numbers known as <a href="https://en.wikipedia.org/wiki/Cepstrum">cepstral</a> coefficients. The dimension of this vector is usually small—sometimes as low as 10, although more accurate systems may have dimension 32 or more. The final output of the HMM is a sequence of these vectors.</p>
<p>To decode the speech into text, groups of vectors are matched to one or more <a href="https://en.wikipedia.org/wiki/Phoneme">phonemes</a>—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.</p>
<p>One can imagine that this whole process may be computationally expensive. In many modern speech recognition systems, neural networks are used to simplify the speech signal using techniques for feature transformation and dimensionality reduction <em>before</em> HMM recognition. Voice activity detectors (VADs) are also used to reduce an audio signal to only the portions that are likely to contain speech. This prevents the recognizer from wasting time analyzing unnecessary parts of the signal.</p>
<p>Fortunately, as a Python programmer, you don’t have to worry about any of this. A number of speech recognition services are available for use online through an API, and many of these services offer <a href="https://realpython.com/api-integration-in-python/">Python SDKs</a>.</p>
</section>


<section class="section2" id="installing-speechrecognition"><h2>Installing SpeechRecognition</h2>
<p>SpeechRecognition is compatible with Python 2.6, 2.7 and 3.3+, but requires some <a href="https://github.com/Uberi/speech_recognition#requirements">additional installation steps for Python 2</a>. For this tutorial, I’ll assume you are using Python 3.3+.</p>
<p>You can install SpeechRecognition from a terminal with pip:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> pip install SpeechRecognition
</code></pre></div>
<p>Once installed, you should verify the installation by opening an interpreter session and typing:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">speech_recognition</span> <span class="k">as</span> <span class="nn">sr</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">sr</span><span class="o">.</span><span class="n">__version__</span>
<span class="go">'3.8.1'</span>
</code></pre></div>
<div class="alert alert-primary" role="alert">
<p><strong>Note:</strong> The version number you get might vary. Version 3.8.1 was the latest at the time of writing.</p>
</div>
<p>Go ahead and keep this session open. You’ll start to work with it in just a bit.</p>
<p>SpeechRecognition <em>will</em> work out of the box if all you need to do is work with existing audio files. Specific use cases, however, require a few dependencies. Notably, the PyAudio package is needed for capturing microphone input.</p>
<p>You’ll see which dependencies you need as you read further. For now, let’s dive in and explore the basics of the package.</p>


<section class="section2" id="the-recognizer-class"><h2>The <code>Recognizer</code> Class</h2>
<p>All of the magic in SpeechRecognition happens with the <code>Recognizer</code> class.</p>
<p>The primary purpose of a <code>Recognizer</code> instance is, of course, to recognize speech. Each instance comes with a variety of settings and functionality for recognizing speech from an audio source.</p>
<p>Creating a <code>Recognizer</code> instance is easy. In your current interpreter session, just type:</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">r</span> <span class="o">=</span> <span class="n">sr</span><span class="o">.</span><span class="n">Recognizer</span><span class="p">()</span>
</code></pre></div>
<p>Each <code>Recognizer</code> instance has seven methods for recognizing speech from an audio source using various APIs. These are:</p>
<ul>
<li><code>recognize_bing()</code>: <a href="https://azure.microsoft.com/en-us/services/cognitive-services/speech/">Microsoft Bing Speech</a></li>
<li><code>recognize_google()</code>: <a href="https://w3c.github.io/speech-api/speechapi.html">Google Web Speech API</a></li>
<li><code>recognize_google_cloud()</code>: <a href="https://cloud.google.com/speech/">Google Cloud Speech</a> - requires installation of the google-cloud-speech package</li>
<li><code>recognize_houndify()</code>: <a href="https://www.houndify.com/">Houndify</a> by SoundHound</li>
<li><code>recognize_ibm()</code>: <a href="https://www.ibm.com/watson/services/speech-to-text/">IBM Speech to Text</a></li>
<li><code>recognize_sphinx()</code>: <a href="https://cmusphinx.github.io/">CMU Sphinx</a> - requires installing PocketSphinx</li>
<li><code>recognize_wit()</code>: <a href="https://wit.ai/">Wit.ai</a></li>
</ul>
<p>Of the seven, only <code>recognize_sphinx()</code> works offline with the CMU Sphinx engine. The other six all require an internet connection.</p>
<p>A full discussion of the features and benefits of each API is beyond the scope of this tutorial. Since SpeechRecognition ships with a default API key for the Google Web Speech API, you can get started with it right away. For this reason, we’ll use the Web Speech API in this guide. The other six APIs all require authentication with either an API key or a username/password combination. For more information, consult the SpeechRecognition <a href="https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst">docs</a>.</p>
<div class="alert alert-primary" role="alert">
<p><strong>Caution:</strong> The default key provided by SpeechRecognition is for testing purposes only, and <strong>Google may revoke it at any time</strong>. It is <em>not</em> a good idea to use the Google Web Speech API in production. Even with a valid API key, you’ll be limited to only 50 requests per day, and <a href="http://www.chromium.org/developers/how-tos/api-keys">there is no way to raise this quota</a>. Fortunately, SpeechRecognition’s interface is nearly identical for each API, so what you learn today will be easy to translate to a real-world project.</p>
</div>
<p>Each <code>recognize_*()</code> method will throw a <code>speech_recognition.RequestError</code> exception if the API is unreachable. For <code>recognize_sphinx()</code>, this could happen as the result of a missing, corrupt or incompatible Sphinx installation. For the other six methods, <code>RequestError</code> may be thrown if quota limits are met, the server is unavailable, or there is no internet connection.</p>
<p>Ok, enough chit-chat. Let’s get our hands dirty. Go ahead and try to call <code>recognize_google()</code> in your interpreter session.</p>
<div class="highlight python repl"><span class="repl-toggle" title="Toggle REPL prompts and output">&gt;&gt;&gt;</span><pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="o">.</span><span class="n">recognize_google</span><span class="p">()</span>
</code></pre></div>





<img class="card-img-top m-0 p-0 embed-responsive-item rounded" style="object-fit: contain;" alt="Python Speech Recognition" src="https://files.realpython.com/media/The-Ultimate-Guide-To-Speech-Recognition-With-Python_Watermarked.c0511baf27ba.jpg" width="1920" height="1080" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/The-Ultimate-Guide-To-Speech-Recognition-With-Python_Watermarked.c0511baf27ba.jpg&amp;w=480&amp;sig=9c3dbe8b9e5c0a05b993b7908bd6063b12664c1f 480w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/The-Ultimate-Guide-To-Speech-Recognition-With-Python_Watermarked.c0511baf27ba.jpg&amp;w=960&amp;sig=c9fcc84aebc4f9e27842f9955fde304104c0ef3e 960w, https://files.realpython.com/media/The-Ultimate-Guide-To-Speech-Recognition-With-Python_Watermarked.c0511baf27ba.jpg 1920w" sizes="75vw">
