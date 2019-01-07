# CustomAuthorization
A combined authentication wwith the oauth2 provider and a custom authentication using sessions.
We create two apps.

The first one we create as descripted in here : https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html#step-1-minimal-setup

In order to setup our server to obtain tokens.

Now we create the second app custom.

Wise for both apps to have the same user model.

We can easily create a Sign UP with DRF to sign up users later from app to another with the same logic.

In the custom authentication backend we make call to the first's app API with urllib to obtain access token.

We save the refress token in sessions and little before it expired we make a another request in the API,

to obtain another


