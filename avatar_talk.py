from transformers import pipeline
import scipy

def main():


    synthesiser = pipeline("text-to-speech", "suno/bark")

    speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"do_sample": True})

    scipy.io.wavfile.write("bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"])

if __name__ == "__main__":
    main()
