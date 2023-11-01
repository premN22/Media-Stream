
from ibm_watson import ApiException
from ibm_watson import IAMTokenManager
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
from ibm_videostreaming import IBMVideoStreamingV1


api_key = 'YOUR_API_KEY'
region = 'YOUR_REGION'

iam_authenticator = IAMAuthenticator(api_key)
token_manager = IAMTokenManager(iam_authenticator)
token = token_manager.get_token()


video_streaming = IBMVideoStreamingV1(authenticator=iam_authenticator)
video_streaming.set_service_url(f'https://{region}.streaming.cloud.ibm.com')

def create_channel(channel_name):
    try:
        response = video_streaming.create_channel(name=channel_name)
        channel_id = response.get_result()['id']
        return channel_id
    except ApiException as e:
        print('Error creating channel:', e)
        return None

def upload_video(channel_id, video_path):
    try:
        response = video_streaming.upload_video(channel_id=channel_id, filepath=video_path)
        video_id = response.get_result()['id']
        return video_id
    except ApiException as e:
        print('Error uploading video:', e)
        return None

def get_video_url(video_id):
    try:
        response = video_streaming.get_video(video_id=video_id)
        return response.get_result()['playback']['hls_playback_url']
    except ApiException as e:
        print('Error retrieving video URL:', e)
        return None


channel_name = 'MyChannel'
video_path = '/path/to/your/video.mp4'


channel_id = create_channel(channel_name)
if channel_id:
    print('Channel created successfully with ID:', channel_id)
else:
    print('Failed to create channel.')


video_id = upload_video(channel_id, video_path)
if video_id:
    print('Video uploaded successfully with ID:', video_id)
else:
    print('Failed to upload video.')


video_url = get_video_url(video_id)
if video_url:
    print('Video streaming URL:', video_url)
else:
    print('Failed to retrieve video URL.')