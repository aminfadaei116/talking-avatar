# from transformers import pipeline
import scipy

def main():

    import torch

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # synthesiser = pipeline("text-to-speech", "suno/bark")
    #
    # speech = synthesiser("Hello, my dog is cooler than you!", forward_params={"do_sample": True})
    #
    # scipy.io.wavfile.write("bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"])

if __name__ == "__main__":
    main()
