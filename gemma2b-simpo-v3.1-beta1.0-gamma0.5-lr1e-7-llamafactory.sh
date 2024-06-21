llamafactory-cli train \
    --stage dpo \
    --template default\
    --do_train True \
    --model_name_or_path google/gemma-2b \
    --preprocessing_num_workers 16 \
    --finetuning_type full \
    --flash_attn auto \
    --dataset_dir \data \
    --dataset dirty-newsplit-dpo-v3.1 \
    --cutoff_len 2048 \
    --learning_rate 1e-07 \
    --num_train_epochs 1.0 \
    --max_samples 10000 \
    --per_device_train_batch_size 2 \
    --gradient_accumulation_steps 16 \
    --per_device_eval_batch_size 2 \
    --lr_scheduler_type cosine \
    --max_grad_norm 1.0 \
    --logging_steps 10 \
    --save_steps 500 \
    --warmup_steps 500 \
    --optim adamw_torch \
    --packing False \
    --report_to none \
    --output_dir saves/gemma2b-dpo-v3.1-beta1.0-lr1e-7-llamafactory \
    --bf16 True \
    --plot_loss True \
    --ddp_timeout 180000000 \
    --pref_beta 1.0 \
    --pref_ftx 0 \
    --pref_loss simpo \
    --simpo_gamma 0.5 \
    --push_to_hub true \
    --hub_private_repo true \
    --hub_model_id "LmPa/gemma2b-dpo-v3.1-beta1.0-lr1e-7-llamafactory" \
    --hub_strategy all_checkpoints \
    --plot_loss \
    --val_size 0.01 \
    --do_eval true \
    --eval_strategy steps\
    --eval_steps 500 \
    --report_to wandb
