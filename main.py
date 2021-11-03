import test_pipeline as test_pl
import train_pipeline as train_pl

if __name__ == "__main__":
    model = train_pl.train()
    submission = test_pl.test(model)
