def get_estimated_spread(audiences_followers):
    average_audience_followers = 0
    if audiences_followers is None or len(audiences_followers) == 0:
        return 0
    num_followers = len(audiences_followers)
    for follower in audiences_followers:
        average_audience_followers += follower
    average_audience_followers /= num_followers
    estimated_spread = average_audience_followers * (num_followers ** 1.2)

    return estimated_spread