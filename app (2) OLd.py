{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2b35569a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime as dt\n",
    "import numpy as np\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "96665a42",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "926f2dbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7a912c32",
   "metadata": {},
   "outputs": [],
   "source": [
    "#access the database\n",
    "engine = create_engine(\"sqlite:///hawaii.sqlite\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8127498a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#reflect database into the class\n",
    "Base = automap_base()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3ff3376e",
   "metadata": {},
   "outputs": [],
   "source": [
    "#reflect the database into the class\n",
    "Base.prepare(engine, reflect=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "937dcbcf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import app\n",
    "\n",
    "print(\"example __name__ = %s\", __name__)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"example is being run directly.\")\n",
    "else:\n",
    "    print(\"example is being imported\")"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
