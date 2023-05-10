
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import request,jsonify

from cdmsapp.models.feedback import FeedbackModel
from cdmsapp.schemas import FeedbackSchema

blp = Blueprint("Feedback","feedback",description="operation on blueprint")

# @blp.route("/feedback")
# class Feedback(MethodView):
#   @blp.arguments(FeedbackSchema)
#   def add_feedback():
#     data = request.get_json()
#     feedback = Feedback(
#     rating1=data['rating1'], 
#     rating2=data['rating2'],
#     rating3=data['rating3'], 
#     message=data['message'], 
#     rating=data['rating'])
#     feedback.save_to_db()
#     return jsonify(feedback.feedback_id, feedback.rating1, feedback.rating2, feedback.message, feedback.rating3)

# @blp.route('/feedbacks', methods=['GET'])
# def get_feedback():
#     feedback_list = Feedback.query.all()
#     feedback_list_json = []
#     for feedback in feedback_list:
#         feedback_dict = {'id': feedback.feedback_id, 'rating1': feedback.rating1, 'rating2': feedback.rating2, 'message': feedback.message, 'rating3': feedback.rating3}
#         feedback_list_json.append(feedback_dict)
#     return jsonify(feedback_list_json)

@blp.route('/feedback')
class Feedback(MethodView):
    @blp.arguments(FeedbackSchema)
    def post(self,feedback_data):
      # feedback_data = request.json
      # if FeedbackModel.find_by_id(id=feedback_data['feedback_id']):
      #    abort(400, "Feedback Id Already exists")
      feedback = FeedbackModel(
        event_id = feedback_data['event_id'],
        # name = feedback_data['name'],
        # email = feedback_data['email'],
        question1=feedback_data['question1'],
        participant_id = feedback_data['participant_id'],
        # question2=feedback_data['question2'],
        # question3=feedback_data['question3'],
        data=feedback_data['data']
      )
      feedback.save_to_db()

      return jsonify({'message': 'Feedback submitted successfully'})

@blp.route("/feedbacks")
class ItemList(MethodView):
    @blp.response(200, FeedbackSchema(many=True))
    def get(self):
        Feedback = FeedbackModel.get_all_feedback()
       
        return Feedback
    

@blp.route('/feedbackid/<int:feedback_id>')
class Feed(MethodView):
    @blp.response(200,FeedbackSchema)
    def get(self,feedback_id):
        feedback = FeedbackModel.find_by_id(feedback_id)
        if not feedback:
          abort(404,message="Feedback Not found")
        return feedback
      
    def delete(self,feedback_id):
      feedback = FeedbackModel.find_by_id(feedback_id)
      if not feedback:
        abort(404, "No feedbacks")
      feedback.delete_from_db()
      return {"message": "feedback deleted."}, 200 
      
      

