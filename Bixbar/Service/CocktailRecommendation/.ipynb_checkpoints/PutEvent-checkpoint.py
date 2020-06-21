{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "import json"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class EventHandle:\n",
    "\n",
    "    def putEvent(TIMESTAMP: str, USER_ID: str, ITEM_ID: str):\n",
    "        try:\n",
    "            personalize_events = boto3.client(service_name='personalize-events')\n",
    "            personalize_events.put_events(\n",
    "             trackingId = '840f1b0b-301b-47a7-9526-cf2684be90f9',\n",
    "             userId= USER_ID,\n",
    "             sessionId = 'session_id',\n",
    "             eventList = [ {\n",
    "             'eventId': 'event1',\n",
    "             'sentAt': TIMESTAMP,\n",
    "             'eventType': 'User-item interaction',\n",
    "             'properties': json.dumps({\n",
    "             'TIMESTAMP': TIMESTAMP,\n",
    "             'USER_ID': USER_ID,\n",
    "             'ITEM_ID': ITEM_ID\n",
    "             })\n",
    "             }]\n",
    "            )\n",
    "        except:\n",
    "            return False\n",
    "        return True"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
