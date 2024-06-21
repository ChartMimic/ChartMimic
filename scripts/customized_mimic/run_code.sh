models=(
  "gpt-4-vision-preview"
)

template_type=edit;agent_type=EditAgent

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_checker.py \
    --input_file ${PROJECT_PATH}/results/customized/chartedit_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_interpreter.py \
    --input_file ${PROJECT_PATH}/results/customized/chartedit_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done