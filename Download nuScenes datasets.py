# Databricks notebook source
import os

volume_root = "/Volumes/stuart/aptiv/nuscenes"
os.environ["VOLUMEROOT"] = volume_root

# COMMAND ----------

# MAGIC %sh mkdir -p $VOLUMEROOT/raw

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/v1.0-mini.tgz "https://d36yt3mvayqw5m.cloudfront.net/public/v1.0/v1.0-mini.tgz"

# COMMAND ----------

# MAGIC %sh tar -xzvf $VOLUMEROOT/raw/v1.0-mini.tgz -C $VOLUMEROOT

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/nuScenes-lidarseg-mini-v1.0.tar.bz2 "https://d36yt3mvayqw5m.cloudfront.net/public/nuscenes-lidarseg-v1.0/nuScenes-lidarseg-mini-v1.0.tar.bz2"

# COMMAND ----------

# MAGIC %sh tar -xjvf $VOLUMEROOT/raw/nuScenes-lidarseg-mini-v1.0.tar.bz2 -C $VOLUMEROOT

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/nuScenes-panoptic-v1.0-mini.tar.gz "https://d36yt3mvayqw5m.cloudfront.net/public/nuscenes-panoptic-v1.0/nuScenes-panoptic-v1.0-mini.tar.gz"

# COMMAND ----------

# MAGIC %sh tar tvfz $VOLUMEROOT/raw/nuScenes-panoptic-v1.0-mini.tar.gz

# COMMAND ----------

# MAGIC %sh tar xvfz $VOLUMEROOT/raw/nuScenes-panoptic-v1.0-mini.tar.gz -C /tmp

# COMMAND ----------

# MAGIC %sh cp -r /tmp/nuScenes-panoptic-v1.0-mini/* $VOLUMEROOT

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/nuScenes-map-expansion-v1.3.zip "https://d36yt3mvayqw5m.cloudfront.net/public/v1.0/nuScenes-map-expansion-v1.3.zip"

# COMMAND ----------

# MAGIC %sh unzip -n $VOLUMEROOT/raw/nuScenes-map-expansion-v1.3.zip -d $VOLUMEROOT/maps

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/can_bus.zip "https://d36yt3mvayqw5m.cloudfront.net/public/v1.0/can_bus.zip"

# COMMAND ----------

# MAGIC %sh unzip -n $VOLUMEROOT/raw/can_bus.zip -d $VOLUMEROOT

# COMMAND ----------

# MAGIC %sh wget -O $VOLUMEROOT/raw/nuscenes-prediction-challenge-trajectory-sets.zip "https://www.nuscenes.org/public/nuscenes-prediction-challenge-trajectory-sets.zip"

# COMMAND ----------

# MAGIC %sh unzip -n $VOLUMEROOT/raw/nuscenes-prediction-challenge-trajectory-sets.zip -d $VOLUMEROOT
