from ml.recommendation.recommendation_engine import RecommendationEngine


def evaluate():
    engine = RecommendationEngine()
    engine.train()

    print("=" * 60)
    print("Recommendation Engine Evaluation")
    print("=" * 60)

    print(f"\nProducts with recommendation data: {len(engine.cooccurrence)}")

    if not engine.cooccurrence:
        print("No recommendation data available.")
        return

    sample_product = next(iter(engine.cooccurrence.keys()))

    print(f"\nSample Product:\n{sample_product}")

    recommendations = engine.recommend(sample_product)

    print("\nRecommendations:\n")

    if recommendations:
        for recommendation in recommendations:
            print(recommendation)
    else:
        print("No recommendations found.")


if __name__ == "__main__":
    evaluate()