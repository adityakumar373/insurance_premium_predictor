from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    insurance_premium_category: str = Field(..., description="Predicted insurance premium category", example="High")
    confidence: float = Field(..., description="Confidence score of the prediction range(0-1)", example=0.85)
    model_version: str = Field(..., description="Version of the model used for prediction")
    class_probabilities: Dict[str, float] = Field({}, description="Probabilities for each class",example={"Low": 0.1, "Medium": 0.3, "High": 0.6})